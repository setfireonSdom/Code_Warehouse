```bash
echo hello terminal

// 查看工作目录
pwd

// 查看目录内容
ls

// showing more details
ls -l

ls --help

// cd意思是change directory
cd 

// go back a folder level
cd ..

// go back two folders
cd ../..

// you can see what's in a file with more <filename>
more package.json

// empty the terminal
clear

// make a new folder,mkdir stands for "make directory".
mkdir website
// 跨目录创建文件夹，指定路径创建文件夹，client目录必须存在。
mkdir client/<new_folder_name>

// create a new file
touch index.html

touch <path/filename>


// copy a file
cp <file> <destination>
cp background.jpg images/
// 把 website-boilerplate 文件夹及其所有内容递归复制到 toms-website 文件夹
cp -r website-boilerplate toms-website


// remove a file
rm background.jpg
// remove directories and their contents recursively
rm -r fonts

// rename file,mv stands for "move", it can rename or move something. 
mv <filename> <new_filename>
mv <file> <destination>
// mv 后面可以接文件的具体路径，将具体路径的文件移动到其他位置。

// find things or view a file tree.
find
find <filename>
// You can use it to search for something with find -name <filename>
find -name <filename>

// remove a folder.rmdir stands for "remove directory".
rmdir <directory_name>

// You can print to a file instead of the terminal with echo text >> filename
echo text >> filename
echo I made this boilerplate >> README.md

// 
exit


```