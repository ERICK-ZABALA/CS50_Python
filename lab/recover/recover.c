#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
// TODO
// *** Open memory card
// File *f = fopen(filename, "r");
// 3 bytes 0xff 0xd8 0xff 0xe[0-f]
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    if (strcmp(argv[1], "card.raw") != 0)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");

    if (!file)
    {
        printf("File card.raw not Open\n");
        return 1;
    }
    printf("File card.raw Open...\n");


// Look for beginning of a JPEG
// Read Files fread(data, size, number, inptr);
// data: pointer to where to store data you are reading
// size: size of each element to read 512 bytes
// number: number of elements to read (3 bytes 0xff 0xd8 0xff 0xe[0-f])
// inptr: FILE * to read from (file name that we need to read)
// address pointer = 8 bytes in computer ex. 0x7ffda0a4767c


    BYTE buffer[512]; // 512 bytes to read that is the block
    int BLOCK_SIZE = sizeof(BYTE); // size of BYTE

    int counter = 0;
    int result = 0;
    int counter_image = 0;
    char filename[8];

    while (fread(buffer, BLOCK_SIZE, 512, file) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
        {
            // printf("match 4 bytes\n");
            counter = counter + 1;
            // First JPEG
            if (counter == 1)
            {
                // make a new file jpg ex. filename000.jpg
                sprintf(filename, "%03i.jpg", (counter_image));
                FILE *img = fopen(filename, "w");
                fwrite(buffer, BLOCK_SIZE, 512, img);
                fclose(img);
                counter_image = counter_image + 1;
                counter = counter + 1;
            }
            else
            {

                // printf("block 2do 512 bytes number: %i\n", counter);
                // make a new file jpg ex. filename000.jpg
                sprintf(filename, "%03i.jpg", (counter_image));
                FILE *img = fopen(filename, "w");
                fwrite(buffer, BLOCK_SIZE, 512, img);
                fclose(img);
                counter_image = counter_image + 1;
                counter = 0;
                // printf(" ingreso al else %i\n", counter_image);

            }
        }
        else if (counter_image > 0)
        {
            // Perform capture all 512 bytes after 1st block hit to complete all image.
            FILE *img = fopen(filename, "a");
            fwrite(buffer, BLOCK_SIZE, 512, img);
            fclose(img);
        }

    }
    fclose(file);
}


