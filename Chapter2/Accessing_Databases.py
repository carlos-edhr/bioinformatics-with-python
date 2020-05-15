from Bio import Entrez, Medline, SeqIO

Entrez.email = "carlos.edhr@gmail.com" 

#This gives you the list of available databases
# handle = Entrez.einfo()
# rec = Entrez.read(handle)
# print(rec)

handle = Entrez.esearch(db="nucleotide", term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]')
rec_list = Entrez.read(handle)
if rec_list['RetMax'] < rec_list['Count']:
    handle = Entrez.esearch(db="nucleotide", term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]',
                            retmax=rec_list['Count'])
    rec_list = Entrez.read(handle)

id_list = rec_list['IdList']
hdl = Entrez.efetch(db='nucleotide', id=id_list, rettype='gb', retmax=rec_list['Count'])

recs = list(SeqIO.parse(hdl, 'gb'))

for rec in recs:
    if rec.name == 'KM288867':
        break
print(rec.name)
print(rec.description)

for feature in rec.features:
    if feature.type == 'gene':
        print(feature.qualifiers['gene'])
    elif feature.type == 'exon':
        loc = feature.location
        print('Exon', loc.start, loc.end, loc.strand)
    else:
        print('not processed:\n%s' % feature)

for name, value in rec.annotations.items():
    print('%s=%s' % (name, value))

print(len(rec.seq))

refs = rec.annotations['references']
for ref in refs:
    if ref.pubmed_id != '':
        print(ref.pubmed_id)
        handle = Entrez.efetch(db="pubmed", id=[ref.pubmed_id],
                                rettype="medline", retmode="text")
        records = Medline.parse(handle)
        for med_rec in records:
            for k, v in med_rec.items():
                print('%s: %s' % (k, v))