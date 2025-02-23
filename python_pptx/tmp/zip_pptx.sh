


FILE=test1
cd _unzip_file/${FILE}
/c/"Program Files"/7-Zip/7z  a  -tzip  ../../${FILE}.pptx ./
cd ../../

#echo "org---------------------------"
#/c/"Program Files"/7-Zip/7z  l  -tzip test1/test1.pptx
#echo "rev---------------------------"
#/c/"Program Files"/7-Zip/7z  l  -tzip test1.pptx 


FILE=test2
cd _unzip_file/${FILE}
/c/"Program Files"/7-Zip/7z  a  -tzip  ../../${FILE}.pptx ./
cd ../../
