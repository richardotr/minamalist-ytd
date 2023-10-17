
#define _CRT_SECURE_NO_DEPRECATE 1
#define _CRT_NONSTDC_NO_DEPRECATE 1

#define ESC 27

#include <windows.h>
#include <stdio.h>
#include <conio.h>
#include <string.h>
// #include <stdlib.h>
// dont need ctype

void sup( char lmfao[] )
{
    STARTUPINFO si;
    PROCESS_INFORMATION pi;
    //lmfao = "-h";//"https://www.youtube.com/watch?v=xgNeFTCzpgo";
    char rex = '"';
    char kick[200] = "nx_ref --path product --ffmpeg-location bin -x --audio-format";
    char steptype[] = " mp3 ";

    strncat(kick, steptype, strlen(steptype));
    strncat(kick, &rex, 1);
    strncat(kick, lmfao, strlen(lmfao));
    strncat(kick, &rex, 1);

    printf("\ncmd: %s\n", kick);

    ZeroMemory( &si, sizeof(si) );
    si.cb = sizeof(si);
    ZeroMemory( &pi, sizeof(pi) );

    // if( argc != 2 )
    // {
    //     printf("Usage: %s [cmdline]\n", argv[0]);
    //     return;
    // }

    // Start the child process. 
    if( !CreateProcess( NULL,   // No module name (use command line)
        kick,        // Command line
        NULL,           // Process handle not inheritable
        NULL,           // Thread handle not inheritable
        FALSE,          // Set handle inheritance to FALSE
        0,              // No creation flags
        NULL,           // Use parent's environment block
        NULL,           // Use parent's starting directory 
        &si,            // Pointer to STARTUPINFO structure
        &pi )           // Pointer to PROCESS_INFORMATION structure
    ) 
    {
        printf( "CreateProcess failed (%d).\n", GetLastError() );
        return;
    }

    // Wait until child process exits.
    WaitForSingleObject( pi.hProcess, INFINITE );

    // Close process and thread handles. 
    CloseHandle( pi.hProcess );
    CloseHandle( pi.hThread );
}

int main(void)
{
    printf("youtube downloder settings:\nuse EU proxy server: false\ntarget format: MP3\nclient: chrome driver 3.7.23\ndirectory: \ncustom output name: false\n");
    printf("paste link ex.(https://www.youtube.com/watch?v=I9VfWCyCagQ)\n");
    
    int core = 1;
    while (core == 1)
    {
        printf("\n: ");
        char rewram[101] = "";
        scanf("%100s", rewram);
        sup(rewram);

        printf("\npress [a] to pol again OR [ESC]to close\n\n");
        
        int loop1 = 1;
        while (loop1 == 1)
        {
            char darby = getch();
            if (darby == 'a') 
            {
                loop1 = 0;
                // continue
            } else if (darby == ESC) 
            {
                core = 0;
                loop1 = 0;
            } else 
            {
                printf("\nunknown key! click [ESC] or [a]\n");
            }
        }
    }

    return 0;
}
