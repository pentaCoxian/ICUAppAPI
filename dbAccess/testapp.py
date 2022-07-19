import itertools
kouho = ['ay', 'term', 'cno', 'title_e', 'title_j', 'lang', 'instructor', 'unit_e', 'koma_lecture_e', 'koma_seminar_e', 'koma_labo_e', 'koma_act_e', 'koma_int_e', 'descreption', 'descreption_j', 'goals', 'goals_j', 'content', 'content_j', 'lang_of_inst', 'pollicy', 'individual_study', 'ref', 'notes', 'schedule', 'url']
kouho = ['term', 'cno', ('title_e', 'title_j'), 'instructor', ('descreption', 'descreption_j'), ('goals', 'goals_j'), ('content', 'content_j'), 'lang_of_inst', 'pollicy',  'ref', 'notes', 'schedule']
combs=[]
for i in range(1, len(kouho)+1):
    els = [list(x) for x in itertools.combinations(kouho, i)]
    combs.extend(els)
print(len(combs))