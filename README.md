# simpligo-ranker

## NILC
Este trabalho é parte do meu doutorado no ICMC-USP, vinculado ao laboratório do NILC - Núcleo Interinstitucional de Linguística Computacional.

[http://www.nilc.icmc.usp.br/nilc/index.php](http://www.nilc.icmc.usp.br/nilc/index.php)

## Licença
[AGPL 3.0](https://www.gnu.org/licenses/agpl-3.0.pt-br.html)

## Citação
````
@inproceedings{leal2019ranking,
    author = {Sidney Evaldo Leal and Vanessa Maia Aguiar de Magalhães and Magali Sanches Duran and Sandra Maria Aluísio},
    title = {Avaliação Automática da Complexidade de Sentenças do Português Brasileiro para o Domínio Rural},
    booktitle = {STIL 2019 - Symposium in Information and Human Language Technology},
    year = {2019},
    pages = {?–?},
    month = {Outubro},
    date = {15-18},
    address = {Salvador, Bahia, Brasil},
}
````

## Resultado do algoritmo de seleção de *features Permutation Importance* no regressor:

|ranking | *Feature*   |    Peso    |
|:-:|---|:-:|
|1 | brunet | 0,011193|
|2 | simple_word_ratio | 0,008652|
|3 | log_pos_conn_ratio | 0,002465|
|4 | flesch | 0,002249|
|5 | punctuation_ratio | 0,001815|
|6 | idade_aquisicao_std | 0,001809|
|7 | dep_distance | 0,001587|
|8 | third_person_pronouns | 0,001263|
|9 | dalechall_adapted | 0,001046|
|10 | content_word_max | 0,000957|
|11 | punctuation_diversity | 0,000881|
|12 | sentences_with_one_clause | 0,000819|
|13 | familiaridade_std | 0,000744|
|14 | content_words_ambiguity | 0,000703|
|15 | logic_operators | 0,000698|
|16 | syllables_per_content_word | 0,000583|
|17 | passive_ratio | 0,000580|
|18 | adjunct_per_clause | 0,000570|
|19 | aux_plus_PCP_per_sentence | 0,000560|
|20 | content_word_min | 0,000547|
|21 | verbs_min | 0,000542|
|22 | familiaridade_mean | 0,000537|
|23 | nouns_ambiguity | 0,000536|
|24 | cau_neg_conn_ratio | 0,000521|
|25 | ratio_function_to_content_words | 0,000512|
|26 | ratio_coordinate_conjunctions | 0,000497|
|27 | adverbs_before_main_verb_ratio | 0,000492|
|28 | verbs_max | 0,000482|
|29 | sentence_length_min | 0,000481|
|30 | indicative_pluperfect_ratio | 0,000475|
|31 | sentences_with_four_clauses | 0,000461|
|32 | adverbs_diversity_ratio | 0,000454|
|33 | sentences_with_three_clauses | 0,000443|
|34 | idade_aquisicao_4_55_ratio | 0,000437|
|35 | words_per_sentence | 0,000425|
|36 | frazier | 0,000415|
|37 | easy_conjunctions_ratio | 0,000392|
|38 | idade_aquisicao_25_4_ratio | 0,000387|
|39 | sentences_with_five_clauses | 0,000366|
|40 | honore | 0,000365|
|41 | apposition_per_clause | 0,000362|
|42 | non_svo_ratio | 0,000358|
|43 | adjectives_ambiguity | 0,000337|
|44 | participle_verbs | 0,000337|
|45 | cau_pos_conn_ratio | 0,000333|
|46 | max_noun_phrase | 0,000319|
|47 | words | 0,000313|
|48 | adjective_diversity_ratio | 0,000304|
|49 | sentences_with_six_clauses | 0,000301|
|50 | verbs | 0,000295|
|51 | familiaridade_25_4_ratio | 0,000290|
|52 | prepositions_per_sentence | 0,000285|
|53 | clauses_per_sentence | 0,000268|
|54 | adjectives_min | 0,000261|
|55 | adverbs | 0,000252|
|56 | indicative_future_ratio | 0,000250|
|57 | verbal_time_moods_diversity | 0,000240|
|58 | relative_pronouns_diversity_ratio | 0,000239|
|59 | function_words | 0,000233|
|60 | content_density | 0,000212|
|61 | sentence_length_max | 0,000205|
|62 | concretude_4_55_ratio | 0,000204|
|63 | non-inflected_verbs | 0,000204|
|64 | third_person_possessive_pronouns | 0,000202|
|65 | tmp_pos_conn_ratio | 0,000199|
|66 | concretude_mean | 0,000186|
|67 | short_sentence_ratio | 0,000182|
|68 | conn_ratio | 0,000170|
|69 | mean_noun_phrase | 0,000165|
|70 | verbs_ambiguity | 0,000163|
|71 | hard_conjunctions_ratio | 0,000163|
|72 | and_ratio | 0,000162|
|73 | preposition_diversity | 0,000156|
|74 | idade_aquisicao_55_7_ratio | 0,000156|
|75 | inflected_verbs | 0,000154|
|76 | gunning_fox | 0,000148|
|77 | idade_aquisicao_mean | 0,000145|
|78 | ttr | 0,000145|
|79 | idade_aquisicao_1_25_ratio | 0,000144|
|80 | hypernyms_verbs | 0,000142|
|81 | indicative_imperfect_ratio | 0,000142|
|82 | infinite_subordinate_clauses | 0,000139|
|83 | std_noun_phrase | 0,000138|
|84 | concretude_std | 0,000138|
|85 | function_word_diversity | 0,000134|
|86 | relative_clauses | 0,000129|
|87 | long_sentence_ratio | 0,000129|
|88 | subjunctive_present_ratio | 0,000127|
|89 | adverbs_max | 0,000124|
|90 | medium_long_sentence_ratio | 0,000120|
|91 | postponed_subject_ratio | 0,000119|
|92 | subjunctive_imperfect_ratio | 0,000117|
|93 | words_before_main_verb | 0,000114|
|94 | add_pos_conn_ratio | 0,000111|
|95 | yngve | 0,000110|
|96 | medium_short_sentence_ratio | 0,000109|
|97 | indefinite_pronouns_diversity | 0,000107|
|98 | sentences | 0,000105|
|99 | subjunctive_future_ratio | 0,000104|
|100 | pronouns_min | 0,000103|
|101 | content_word_standard_deviation | 0,000102|
|102 | coordinate_conjunctions_per_clauses | 0,000102|
|103 | negation_ratio | 0,000100|
|104 | pronoun_diversity | 0,000097|
|105 | concretude_55_7_ratio | 0,000096|
|106 | adverbs_min | 0,000095|
|107 | familiaridade_1_25_ratio | 0,000093|
|108 | verb_diversity | 0,000092|
|109 | familiaridade_55_7_ratio | 0,000092|
|110 | imageabilidade_4_55_ratio | 0,000091|
|111 | imageabilidade_55_7_ratio | 0,000089|
|112 | gerund_verbs | 0,000089|
|113 | abstract_nouns_ratio | 0,000088|
|114 | if_ratio | 0,000085|
|115 | content_word_diversity | 0,000078|
|116 | ratio_subordinate_conjunctions | 0,000075|
|117 | min_cw_freq | 0,000073|
|118 | first_person_pronouns | 0,000073|
|119 | add_neg_conn_ratio | 0,000072|
|120 | concretude_25_4_ratio | 0,000072|
|121 | personal_pronouns | 0,000070|
|122 | sentences_per_paragraph | 0,000069|
|123 | imageabilidade_std | 0,000069|
|124 | prepositions_per_clause | 0,000068|
|125 | familiaridade_4_55_ratio | 0,000067|
|126 | indicative_present_ratio | 0,000067|
|127 | log_neg_conn_ratio | 0,000064|
|128 | cw_freq | 0,000063|
|129 | min_noun_phrase | 0,000059|
|130 | temporal_adjunct_ratio | 0,000056|
|131 | oblique_pronouns_ratio | 0,000055|
|132 | nouns_min | 0,000055|
|133 | indicative_condition_ratio | 0,000052|
|134 | indefinite_pronoun_ratio | 0,000052|
|135 | indicative_preterite_perfect_ratio | 0,000052|
|136 | sentences_with_zero_clause | 0,000051|
|137 | adjective_ratio | 0,000049|
|138 | pronoun_ratio | 0,000049|
|139 | dialog_pronoun_ratio | 0,000047|
|140 | imageabilidade_mean | 0,000047|
|141 | pronouns_max | 0,000046|
|142 | infinitive_verbs | 0,000046|
|143 | sentence_length_standard_deviation | 0,000045|
|144 | imageabilidade_25_4_ratio | 0,000044|
|145 | relative_pronouns_ratio | 0,000042|
|146 | sentences_with_seven_more_clauses | 0,000041|
|147 | named_entity_ratio_sentence | 0,000035|
|148 | or_ratio | 0,000034|
|149 | nouns_max | 0,000033|
|150 | adverbs_ambiguity | 0,000030|
|151 | noun_ratio | 0,000029|
|152 | sentences_with_two_clauses | 0,000022|
|153 | named_entity_ratio_text | 0,000022|
|154 | tmp_neg_conn_ratio | 0,000020|
|155 | first_person_possessive_pronouns | 0,000017|
|156 | content_words | 0,000015|
|157 | noun_diversity | 0,000013|
|158 | second_person_pronouns | 0,000012|
|159 | adjectives_max | 0,000008|
|160 | subordinate_clauses | 0,000007|
|161 | concretude_1_25_ratio | 0,000004|
|162 | paragraphs | 0,000000|
|163 | adjacent_refs | 0,000000|
|164 | anaphoric_refs | 0,000000|
|165 | adj_arg_ovl | 0,000000|
|166 | arg_ovl | 0,000000|
|167 | adj_stem_ovl | 0,000000|
|168 | stem_ovl | 0,000000|
|169 | adj_cw_ovl | 0,000000|
|170 | adj_mean | 0,000000|
|171 | adj_std | 0,000000|
|172 | all_mean | 0,000000|
|173 | all_std | 0,000000|
|174 | paragraph_mean | 0,000000|
|175 | paragraph_std | 0,000000|
|176 | givenness_mean | 0,000000|
|177 | givenness_std | 0,000000|
|178 | span_mean | 0,000000|
|179 | span_std | 0,000000|
|180 | second_person_possessive_pronouns | 0,000000|
|181 | adjectives_standard_deviation | 0,000000|
|182 | adverbs_standard_deviation | 0,000000|
|183 | imageabilidade_1_25_ratio | 0,000000|
|184 | nouns_standard_deviation | 0,000000|
|185 | subtitles | 0,000000|
|186 | pronouns_standard_deviation | 0,000000|
|187 | demonstrative_pronoun_ratio | 0,000000|
|188 | coreference_pronoum_ratio | 0,000000|
|189 | verbs_standard_deviation | 0,000000 |
