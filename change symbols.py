import re

s=str('Any@# woie>> лю??бу?ю. с..т<ок<у, а )я уда(лю в=се зна+ки пр??ип>енан<ия:')
s=re.sub('\2', '', s)
#s=re.sub('[.,:;?!@<#$%>^&*()_+=~`]', '', s)
print(s)