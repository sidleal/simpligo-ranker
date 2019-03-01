import numpy
import pandas
import random
import pickle

from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.pipeline import Pipeline

input_size = 378 #189*2
pipeline = None


def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(30, input_dim=input_size, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation="sigmoid"))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

class Quick(object):
    def particao(self, a, ini, fim):
        pivo = a[fim - 1]
        start = ini
        end = ini
        for i in range(ini, fim):
            input = numpy.append(pivo['feats'],a[i]['feats'])
            prediction = pipeline.predict(numpy.array([input]))
            #print(pivo)
            #print(a[i])
            print(pivo['level'], a[i]['level'], prediction)
            print(pivo['text'])
            print(a[i]['text'])
            if prediction > 0.5 and pivo['text'] != a[i]['text']: #a[i] mais complexo que pivo
            #if a[i] > pivo:
                end += 1
            else:
                end += 1
                start += 1
                aux = a[start - 1]
                a[start - 1] = a[i]
                a[i] = aux
        return start - 1

    def quickSort(self, a, ini, fim):
        if ini < fim:
            pp = self.randparticao(a, ini, fim)
            self.quickSort(a, ini, pp)
            self.quickSort(a, pp + 1, fim)
        return a

    def randparticao(self, a, ini, fim):
        rand = random.randrange(ini, fim)
        aux = a[fim - 1]
        a[fim - 1] = a[rand]
        a[rand] = aux
        return self.particao(a, ini, fim)

pandas.set_option('display.max_colwidth', -1)
# load dataset
df = pandas.read_csv("data/pss2_features_pairs_align.tsv", delimiter='\t', header=0)

estimators = []
with open('models/pss2_std_scaler_class.pickle', 'rb') as handle:
    std_scaler = pickle.load(handle)
    estimators.append(('standardize', std_scaler))

estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=10, verbose=1)
estimator.model = load_model("models/model_pss2_class.h5")

estimators.append(('mlp', estimator))
pipeline = Pipeline(estimators)

new_list = []
for i in range(0, len(df)):
    line_from = {'level': '', 'text': df.iloc[i, 4], 'feats': numpy.asanyarray(df.iloc[i, 5:194])}
    line_to = {'level': '', 'text': df.iloc[i, 194], 'feats': numpy.asanyarray(df.iloc[i, 195:384])}

    if df.iloc[i,1] == 'ORI->NAT':
        if df.iloc[i,3] == 0:
            line_from['level'] = 'ORI'
            line_to['level'] = 'NAT'
        else:
            line_from['level'] = 'NAT'
            line_to['level'] = 'ORI'
    else:
        if df.iloc[i, 3] == 0:
            line_from['level'] = 'NAT'
            line_to['level'] = 'STR'
        else:
            line_from['level'] = 'STR'
            line_to['level'] = 'NAT'

    new_list.append(line_from)
    new_list.append(line_to)

print(len(new_list))

ab = numpy.append(new_list[1]['feats'],new_list[10]['feats'])

prediction = pipeline.predict(numpy.array([ab]))
print(prediction)

q = Quick()
ordered_list = q.quickSort(new_list, 0, len(new_list))

dest = open("data/pss2_ranking_global.tsv", "w", encoding="utf-8")

dest.write('idx\tlevel\ttext\tadjective_ratio\tadverbs\tcontent_words\tflesch\tfunction_words\tsentences_per_paragraph\tsyllables_per_content_word\twords_per_sentence\tnoun_ratio\tparagraphs\tsentences\twords\tpronoun_ratio\tverbs\tlogic_operators\tand_ratio\tif_ratio\tor_ratio\tnegation_ratio\tcw_freq\tmin_cw_freq\thypernyms_verbs\tbrunet\thonore\tpersonal_pronouns\tttr\tconn_ratio\tadd_neg_conn_ratio\tadd_pos_conn_ratio\tcau_neg_conn_ratio\tcau_pos_conn_ratio\tlog_neg_conn_ratio\tlog_pos_conn_ratio\ttmp_neg_conn_ratio\ttmp_pos_conn_ratio\tadjectives_ambiguity\tadverbs_ambiguity\tnouns_ambiguity\tverbs_ambiguity\tyngve\tfrazier\tdep_distance\tcontent_density\twords_before_main_verb\tadjacent_refs\tanaphoric_refs\tadj_arg_ovl\targ_ovl\tadj_stem_ovl\tstem_ovl\tadj_cw_ovl\tadj_mean\tadj_std\tall_mean\tall_std\tparagraph_mean\tparagraph_std\tgivenness_mean\tgivenness_std\tspan_mean\tspan_std\tapposition_per_clause\tclauses_per_sentence\tprepositions_per_clause\tadjunct_per_clause\tprepositions_per_sentence\trelative_clauses\taux_plus_PCP_per_sentence\tcoordinate_conjunctions_per_clauses\tratio_coordinate_conjunctions\tfirst_person_possessive_pronouns\tfirst_person_pronouns\tgerund_verbs\tinfinitive_verbs\tinflected_verbs\tnon-inflected_verbs\tparticiple_verbs\tpassive_ratio\tsecond_person_possessive_pronouns\tsecond_person_pronouns\tsentences_with_five_clauses\tsentences_with_four_clauses\tsentences_with_one_clause\tsentences_with_seven_more_clauses\tsentences_with_six_clauses\tsentences_with_three_clauses\tsentences_with_two_clauses\tsentences_with_zero_clause\tsimple_word_ratio\tratio_subordinate_conjunctions\tthird_person_possessive_pronouns\tthird_person_pronouns\tadjective_diversity_ratio\tadjectives_max\tadjectives_min\tadjectives_standard_deviation\tadverbs_diversity_ratio\tadverbs_max\tadverbs_min\tadverbs_standard_deviation\tconcretude_mean\tconcretude_std\tconcretude_1_25_ratio\tconcretude_25_4_ratio\tconcretude_4_55_ratio\tconcretude_55_7_ratio\tcontent_word_diversity\tcontent_word_max\tcontent_word_min\tcontent_word_standard_deviation\tcontent_words_ambiguity\tdalechall_adapted\tverbal_time_moods_diversity\teasy_conjunctions_ratio\tfamiliaridade_mean\tfamiliaridade_std\tfamiliaridade_1_25_ratio\tfamiliaridade_25_4_ratio\tfamiliaridade_4_55_ratio\tfamiliaridade_55_7_ratio\tfunction_word_diversity\tgunning_fox\thard_conjunctions_ratio\tidade_aquisicao_mean\tidade_aquisicao_std\tidade_aquisicao_1_25_ratio\tidade_aquisicao_4_55_ratio\tidade_aquisicao_55_7_ratio\tidade_aquisicao_25_4_ratio\timageabilidade_mean\timageabilidade_std\timageabilidade_1_25_ratio\timageabilidade_25_4_ratio\timageabilidade_4_55_ratio\timageabilidade_55_7_ratio\tindefinite_pronouns_diversity\tmedium_long_sentence_ratio\tmax_noun_phrase\tmean_noun_phrase\tmedium_short_sentence_ratio\tmin_noun_phrase\tnamed_entity_ratio_sentence\tnamed_entity_ratio_text\tnoun_diversity\tnouns_max\tnouns_min\tnouns_standard_deviation\tsubtitles\tpostponed_subject_ratio\tpreposition_diversity\tpronoun_diversity\tpronouns_max\tpronouns_min\tpronouns_standard_deviation\tdialog_pronoun_ratio\tpunctuation_diversity\tpunctuation_ratio\tabstract_nouns_ratio\tadverbs_before_main_verb_ratio\tsubjunctive_future_ratio\tindefinite_pronoun_ratio\tindicative_condition_ratio\tindicative_future_ratio\tindicative_imperfect_ratio\tindicative_pluperfect_ratio\tindicative_present_ratio\tindicative_preterite_perfect_ratio\tinfinite_subordinate_clauses\toblique_pronouns_ratio\trelative_pronouns_ratio\tsubjunctive_imperfect_ratio\tsubjunctive_present_ratio\tsubordinate_clauses\ttemporal_adjunct_ratio\tdemonstrative_pronoun_ratio\tcoreference_pronoum_ratio\tnon_svo_ratio\trelative_pronouns_diversity_ratio\tsentence_length_max\tsentence_length_min\tsentence_length_standard_deviation\tshort_sentence_ratio\tstd_noun_phrase\tverb_diversity\tverbs_max\tverbs_min\tverbs_standard_deviation\tlong_sentence_ratio\tratio_function_to_content_words\n')
idx = 1
for item in ordered_list:
    dest.write('%s\t%s\t%s' % (idx, item['level'], item['text']))
    for val in item['feats']:
        dest.write('\t%s' % val)
    dest.write('\n')
    idx+=1

dest.close()
