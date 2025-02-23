
rm -rf _unzip_file/test1
rm -rf _unzip_file/test2
rm -rf work/*

#unzip test1/test1.pptx -d unzip_file/test1
#unzip test2/test2.pptx -d unzip_file/test2
/c/"Program Files"/7-Zip/7z x -tzip -o_unzip_file/test1 test1/test1.pptx
/c/"Program Files"/7-Zip/7z x -tzip -o_unzip_file/test2 test2/test2.pptx

cp _unzip_file/test1/ppt/presentation.xml  work/_org_test1_presentation.xml
cp _unzip_file/test2/ppt/presentation.xml  work/_org_test2_presentation.xml

cp _unzip_file/test1/ppt/slides/slide1.xml  work/_org_test1_slide1.xml
cp _unzip_file/test2/ppt/slides/slide1.xml  work/_org_test2_slide1.xml

#cp _unzip_file/test1/ppt/slides/_rels/slide1.xml.rels  work/_org_test1_slide1.xml.rels
#cp _unzip_file/test2/ppt/slides/_rels/slide1.xml.rels  work/_org_test2_slide2.xml.rels


python xmlpp.py work/_org_test1_presentation.xml  work/_new_test1_presentation.xml
python xmlpp.py work/_org_test2_presentation.xml  work/_new_test2_presentation.xml

python xmlpp.py work/_org_test1_slide1.xml        work/_new_test1_slide1.xml
python xmlpp.py work/_org_test2_slide1.xml        work/_new_test2_slide1.xml

#python xmlpp.py work/_org_test1_slide1.xml.rels  work/_new_test1_slide1.xml.rels
#python xmlpp.py work/_org_test2_slide1.xml.rels  work/_new_test2_slide1.xml.rels

#diff work/_new_test1_presentation.xml work/_new_test2_presentation.xml
