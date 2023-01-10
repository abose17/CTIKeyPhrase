from metric import compute_rouge_l, compute_rouge_n
from cytoolz import curry

# compute_rouge_n(list(concat(summs)), list(concat(abs_sents)), n=1)


# output_summ = 'My name is Nafi Currently I am studying at Kstate My major is CS'
# reference_summ = 'I am Nafi I am a computer science major at Kstate'


reference_summ = 'the crew were training for the boat race which takes place on april 11 . the sunken eight was recovered and returned to oxford ’s base . the choppy conditions were caused by strong wind against the tide creating three successive waves that poured over the boat ’s riggers'



output_summ = 'the oxford university women ’s boat race team were rescued from the thames by the royal national lifeboat institution . crew members were training for the boat race which takes place on saturday . the rowers were returned to oxford ’s base . the royal national lifeboat institution come to the assistance of the oxford university women ’s team'


rouge_n = compute_rouge_n(output_summ.split(), reference_summ.split(), n=1)
print(rouge_n)

rouge_l = compute_rouge_l(output_summ.split(), reference_summ.split())
print(rouge_l)
