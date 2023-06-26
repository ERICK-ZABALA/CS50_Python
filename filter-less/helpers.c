#include "helpers.h"
#include <math.h>
#include <stdlib.h>
#include <cs50.h>
#include <stdio.h>

// Convert image to grayscale

void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Calculate the average pixel value for each pixel
    int average = 0;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            // Set each color value  to the average value
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed = 0;
    int sepiaGreen = 0;
    int sepiaBlue = 0;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sepiaRed = round(((image[i][j].rgbtRed * 0.393) + (image[i][j].rgbtGreen * 0.769) + (image[i][j].rgbtBlue * 0.189)));
            sepiaGreen = round(((image[i][j].rgbtRed * 0.349) + (image[i][j].rgbtGreen * 0.686) + (image[i][j].rgbtBlue * 0.168)));
            sepiaBlue = round(((image[i][j].rgbtRed * 0.272) + (image[i][j].rgbtGreen * 0.534) + (image[i][j].rgbtBlue * 0.131)));
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            // Set each color value  to the average value
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }


    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int tempRed = 0;
    int tempGreen = 0;
    int tempBlue = 0;

    // Swap pixels on horizontally opposite sides
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width/2; j++)
        {
            tempRed = image[i][j].rgbtRed;
            tempGreen = image[i][j].rgbtGreen;
            tempBlue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][width-j-1].rgbtRed;
            image[i][j].rgbtGreen = image[i][width-j-1].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width-j-1].rgbtBlue;

            image[i][width-j-1].rgbtRed = tempRed;
            image[i][width-j-1].rgbtGreen = tempGreen;
            image[i][width-j-1].rgbtBlue = tempBlue;


        }
    }
    return;
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // copy image
    // create a copy array 2D
    RGBTRIPLE copy[height][width];
    // rows
    for (int i = 0; i < height; i++)
    {
        // columns
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // process to make blur in each pixel selected
    // rows
    for (int i = 0; i < height; i++)
    {
        // columns
        int redSum = 0;
        int greenSum = 0;
        int blueSum = 0;
        for (int j = 0; j < width; j++)
        {
            //copy[i][j] = image[i][j];
            get_blur_value(i, j, copy, &redSum, &greenSum, &blueSum);
            image[i][j].rgbtRed = redSum;
            image[i][j].rgbtGreen = greenSum;
            image[i][j].rgbtBlue = blueSum;

        }
    }

    return;
}

void get_blur_value(int i, int j, RGBTRIPLE copy[i][j], int* redSum, int* greenSum, int* blueSum)
{
    *redSum = 0;
    *greenSum = 0;
    *blueSum = 0;
    string sequence[] = {"copy [i][j+1]", "copy [i+1][j+1]",
                         "copy [i+1][j]", "copy [i+1][j-1]",
                         "copy [i][j-1]", "copy [-1+i][-1+j]",
                         "copy [-1+i][j]", "copy [-1+i][j+1]"};

    // tempRed = image[i][j].rgbtRed;
    if (i < 0 | j < 0)
    {

    }
    for (int num = 0; num < 1; num++)
    {
        // position 1
        int total = sizeof(copy);
        int column = sizeof(copy[0]);
        int row = 0;

        if (copy [i][j+1] < sizeof(copy))
        {
            *redSum = 0 + *redSum;
            *greenSum = 0 + *greenSum;
            *blueSum = 0 + *blueSum;
        }
        else
        {
        *redSum = copy [i][j+1].rgbtRed + *redSum;
        *greenSum = copy [i][j+1].rgbtGreen + *greenSum;
        *blueSum = copy [i][j+1].rgbtBlue + *blueSum;
        }
        // position 2
        *redSum = copy [i+1][j+1].rgbtRed + *redSum;
        *greenSum = copy [i+1][j+1].rgbtGreen + *greenSum;
        *blueSum = copy [i+1][j+1].rgbtBlue + *blueSum;
        // position 3
        *redSum = copy [i+1][j].rgbtRed + *redSum;
        *greenSum = copy [i+1][j].rgbtGreen + *greenSum;
        *blueSum = copy [i+1][j].rgbtBlue + *blueSum;
        // position 4
        *redSum = copy [i+1][j-1].rgbtRed + *redSum;
        *greenSum = copy [i+1][j-1].rgbtGreen + *greenSum;
        *blueSum = copy [i+1][j-1].rgbtBlue + *blueSum;
        // position 5
        *redSum = copy [i][j-1].rgbtRed + *redSum;
        *greenSum = copy [i][j-1].rgbtGreen + *greenSum;
        *blueSum = copy [i][j-1].rgbtBlue + *blueSum;
        // position 6
        *redSum = copy [-1+i][-1+j].rgbtRed + *redSum;
        *greenSum = copy [-1+i][-1+j].rgbtGreen + *greenSum;
        *blueSum = copy [-1+i][-1+j].rgbtBlue + *blueSum;
        // position 7
        *redSum = copy [-1+i][j].rgbtRed + *redSum;
        *greenSum = copy [-1+i][j].rgbtGreen + *greenSum;
        *blueSum = copy [-1+i][j].rgbtBlue + *blueSum;
        // position 8
        *redSum = copy [-1+i][j+1].rgbtRed + *redSum;
        *greenSum = copy [-1+i][j+1].rgbtGreen + *greenSum;
        *blueSum = copy [-1+i][j+1].rgbtBlue + *blueSum;
    }

    *redSum = round(*redSum/9.0);
    *greenSum = round(*greenSum/9.0);
    *blueSum = round(*blueSum/9.0);


}