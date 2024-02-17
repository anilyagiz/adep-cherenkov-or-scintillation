import xml.etree.ElementTree as ET
import csv
# XML dosyasını yükle
tree = ET.parse('/kaggle/input/veriveri/SimOutput_nt_Ntuple2_t1.xml')
root = tree.getroot()
with open('veri.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Başlık satırını yaz
    csvwriter.writerow(['pmtno', 'time', 'vector', 'energy'])
    for row in root.iter('row'):
        # Her bir "entry" öğesini belirli bir sırayla alarak sırasıyla "pmtno", "time", "vector" ve "energy" değişkenlerine atar
        pmtno = row[0].attrib['value']
        time = row[1].attrib['value']
        vector = row[2].attrib['value']
        energy = row[3].attrib['value']
        # CSV dosyasına satırı yaz
        csvwriter.writerow([pmtno, time, vector, energy])
print("CSV dosyası oluşturuldu.")