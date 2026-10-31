const fs = require('fs');

// Let's check the sizes of the extracted frames
['scratch/f_02.jpg', 'scratch/f_08.jpg', 'scratch/f_15.jpg'].forEach(f => {
  if (fs.existsSync(f)) {
    console.log(f, 'size:', fs.statSync(f).size);
  }
});
