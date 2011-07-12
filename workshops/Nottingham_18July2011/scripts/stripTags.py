import re, os, sys

dir = "../output/simpleGTech_split/articles"
outdir = "../output/simpleGTech_text/articles"

for file in os.listdir(dir):
	if not file.endswith('.txt'):
		continue

	print(file)
	
	text = open(os.path.join(dir,file),'r').read()
	text_notags = re.sub('<[^>]+>',' ',text)
	text_noentities = re.sub('&[^;]+;','',text_notags)
	text_punc = re.sub(' (?=[,.!:)(\[\]])','',text_noentities)
	new_text = re.sub('\s+',' ',text_punc)

	out = open(os.path.join(outdir,file),'w')
	out.write(new_text)
	out.close()





