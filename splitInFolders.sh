#!/bin/bash

echo "usage - give folder in param1, all files in this folder will be split in sperated folder with 20 files each"
#!/bin/bash

dir_size=200
dir_name="folder"
n=$((`find . -maxdepth 1 -type f | wc -l`/$dir_size+1))
for i in `seq 1 $n`;
do
    mkdir -p "$dir_name$i";
    echo "$dir_name$i";
    find . -maxdepth 1 -type f | head -n $dir_size | xargs -i mv "{}" "$dir_name$i"
done
