#include <math.h>
#include <stdio.h>
#include <float.h>
#include <limits.h>
#include <time.h>
#include <string.h>
#define SIZE 256
 
// Driver code
int first()
{
    double number, squareRoot;
 
    number = 12.5;
 
    // Computing the square root
    squareRoot = sqrt(number);
 
    printf("Square root of %.2lf =  %.2lf",
           number, squareRoot);
    return 0;
}

int second()
{
    double x;
    double result;
    x = 2.3;
    result = sin(x);
    printf("sin(%.2lf) = %.2lf\n",
           x, result);
    x = -2.3;
    result = sin(x);
    printf("sin(%.2lf) = %.2lf\n",
           x, result);
    x = 0;
    result = sin(x);
    printf("sin(%.2lf) = %.2lf\n",
           x, result);
    return 0;
}

#define PI 3.141592654
 
// Driver code
int third()
{
    double arg = 30, result;
 
    // Converting to radian
    arg = (arg * PI) / 180;
 
    result = cos(arg);
    printf("cos of %.2lf radian = %.2lf",
           arg, result);
    return 0;
}

// Driver code
int fourth()
{
    double num = 5.6, result;
    result = log(num);
    printf("log(%.1f) = %.2f",
           num, result);
    return 0;
}

int fifth()
{
    printf("Maximum value of float = %.10e\n",
           FLT_MAX);
    printf("Minimum value of float = %.10e\n",
           FLT_MIN);
    return 0;
}
 
// Driver code
int sixth()
{
    printf("Number of bits in a byte %d\n",
           CHAR_BIT);
    printf("Minimum value of SIGNED CHAR = %d\n",
           SCHAR_MIN);
    printf("Maximum value of SIGNED CHAR = %d\n",
           SCHAR_MAX);
    printf("Maximum value of UNSIGNED CHAR = %d\n",
           UCHAR_MAX);
    printf("Minimum value of SHORT INT = %d\n",
           SHRT_MIN);
    printf("Maximum value of SHORT INT = %d\n",
           SHRT_MAX);
    printf("Minimum value of INT = %d\n",
           INT_MIN);
    printf("Maximum value of INT = %d\n",
           INT_MAX);
    printf("Minimum value of CHAR = %d\n",
           CHAR_MIN);
    printf("Maximum value of CHAR = %d\n",
           CHAR_MAX);
    printf("Minimum value of LONG = %ld\n",
           LONG_MIN);
    printf("Maximum value of LONG = %ld\n",
           LONG_MAX);
    return (0);
}

// Driver code
int seventh(void)
{
    char buffer[SIZE];
    time_t curtime;
    struct tm* loctime;
 
    // Get the current time.
    curtime = time(NULL);
 
    // Convert it to local time
    // representation.
    loctime = localtime(&curtime);
 
    // Print out the date and time
    // in the standard format.
    fputs(asctime(loctime), stdout);
 
    // Print it out
    strftime(buffer, SIZE,
             "Today is %A, %B %d.\n",
             loctime);
 
    fputs(buffer, stdout);
    strftime(buffer, SIZE,
             "The time is %I:%M %p.\n",
             loctime);
    fputs(buffer, stdout);
    return 0;
}

// Driver code
int main()
{
    char str1[100] = "Geeks ",
         str2[100] = " For Geeks";
 
    // Concatenates str1 and str2
    strcat(str1, str2);
 
    // Resultant string is stored
    // in str1
    puts(str1);
 
    return 0;
}

// Driver code
int eighth()
{
    char str1[] = "Geeks",
         str2[] = "gEeks",
         str3[] = "Geeks";
    int result;
 
    // Comparing strings str1
    // and str2
    result = strcmp(str1, str2);
 
    printf("strcmp(str1, str2) = %d\n",
           result);
 
    // Comparing strings str1 and str3
    result = strcmp(str1, str3);
 
    printf("strcmp(str1, str3) = %d\n",
           result);
    return 0;
}

// Driver code
int nineth()
{
    char str1[20] = "Geeks For Geeks";
    char str2[20];
 
    // Copying str1 to str2
    strcpy(str2, str1);
 
    puts(str2);
    return 0;
}

// Driver code
int tenth()
{
    char a[20] = "Program";
    char b[20] = { "Geeks for Geeks" };
    printf("Length of string a = %zu \n",
           strlen(a));
    printf("Length of string b = %zu \n",
           strlen(b));
    return 0;
}