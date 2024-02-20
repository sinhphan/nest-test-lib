import { Injectable } from '@nestjs/common';
import { spawn } from 'child_process';
import * as sharp from 'sharp';
import * as fs from 'fs';
import * as path from 'path';
import * as dicomParser from 'dicom-parser';
import * as jpeg from 'jpeg-js';
@Injectable()
export class AppService {

  getHello(): string {
    const filePath = path.join(process.cwd(), '0002.DCM')

    var newProcess = spawn('python', [
      '../bin/convert_image_to_thumbnail.py',
      filePath,
      "output.jpg"
    ]);
    newProcess.stdout.on('data', function (data) {
      console.log(data.toString());
    });
    return "HELLO 1"
  }

  // getHello(): string {
  //   try {

  //     const filePath = path.join(process.cwd(), '0002.DCM')
  //     const dicomFile = fs.readFileSync(filePath);
  //     // Parse the DICOM file
  //     const dataSet = dicomParser.parseDicom(dicomFile);

  //     // Get the pixel data element
  //     const pixelDataElement = dataSet.elements.x7fe00010;
  //     if (!pixelDataElement) {
  //       console.error('Pixel data not found in DICOM file');
  //       process.exit(1);
  //     }

  //     // Extract pixel data
  //     const pixelData = new Uint16Array(dataSet.byteArray.buffer, pixelDataElement.dataOffset, pixelDataElement.length/ 2);
  //     const width = dataSet.uint16('x00280011');
  //     const height = dataSet.uint16('x00280010');

  //     // Convert pixel data to JPEG using sharp
  //     sharp(Buffer.from(pixelData), {
  //       raw: {
  //         width: width,
  //         height: height,
  //         channels: 3, // DICOM files typically have single-channel (grayscale) images
  //       },
  //     })
  //       .toFormat('jpeg')
  //       .toFile('output.jpg', (err, info) => {
  //         if (err) {
  //           console.error('Error converting DICOM to JPEG:', err);
  //         } else {
  //           console.log('DICOM to JPEG conversion complete');
  //         }
  //       });
  //   } catch (error) {
  //     console.log("🚀 => AppService => getHello => error1:", error)
  //   }

  //   try {
  //     const filePath2 = path.join(process.cwd(), 'at3_1m4_01.tif')
  //     const file2 = fs.readFileSync(filePath2)
  //     sharp(file2).toFile('b.jpg');
  //   } catch (error) {
  //     console.log("🚀 => AppService => getHello => error2:", error)
  //   }

  //   // try {
  //   //   const filePath3 = path.join(process.cwd(), 'sample1.heic')
  //   //   const file3 = fs.readFileSync(filePath3)
  //   //   sharp(file3).toFile('c.jpg');
  //   // } catch (error) {
  //   //   console.log("🚀 => AppService => getHello => error3:", error)
  //   // }

  //   return 'Hello World!';
  // }
}
