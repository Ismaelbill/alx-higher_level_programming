#!/usr/bin/node

/* script that concats 2 files.
 * 
 * The first argument is the file path of the first source file
 * The second argument is the file path of the second source file
 * The third argument is the file path of the destination
 */
const fs = require('fs');
let argv = process.argv;
fs.readFile(argv[2], (err, dataf) => {
   if (err) throw err;

   fs.readFile(argv[3], (err, datas) => {
      if (err) throw err;

      fs.writeFile(argv[4], dataf + datas, (err) => {
         if (err) throw err;
      });
   });
});
