// This macro batch processes all the files in a folder and any
// subfolders in that folder. Opens imgs in bioformats and replace with regular tif.

   requires("1.33s"); 
   dir = getDirectory("Choose a Directory ");
   setBatchMode(true);
   count = 0;
   countFiles(dir);
   n = 0;
   processFiles(dir);
   //print(count+" files processed");
   
   function countFiles(dir) {
      list = getFileList(dir);
      for (i=0; i<list.length; i++) {
          if (endsWith(list[i], "/"))
              countFiles(""+dir+list[i]);
          else
              count++;
      }
  }

   function processFiles(dir) {
      list = getFileList(dir);
      for (i=0; i<list.length; i++) {
          if (endsWith(list[i], "/"))
              processFiles(""+dir+list[i]);
          else {
             showProgress(n++, count);
             path = dir+list[i];
             processFile(path);
          }
      }
  }

    function processFile(path) {
       if (endsWith(path, ".tif")) {
           //open(path);
		   run("Bio-Formats Importer", "open=[" + path + "]");
		   saveAs(path);
           close();
      }
  }
