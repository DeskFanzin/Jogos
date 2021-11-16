#include<stdio.h>

// Biblioteca para o jogo Rei da Pradaria //

int criaspawnx(int a){
    int b = 0;
    if (a==3)
        b = b+370;
    if (a==4 || a==5)
        b = b;
    if (a==6)
        b = b-410;
    if (a==7 || a==8)
        b = b+20;
    if (a==9)
        b = b-410;
    if (a==10 || a==11)
        b = b;
    if (a==1 || a==2)
        b = b+20;
    return b;
}

int criaspawny(int a){
    int c = 0;
    if (a==3)
        c = c+270;
    if (a==4 || a==5)
        c = c+20;
    if (a==6)
        c = c+270;
    if (a==7 || a==8)
        c = c;
    if (a==9)
        c = c-310;
    if (a==10 || a==11)
        c = c+20;
    if (a==1 || a==2)
        c = c;
    return c;
}

int movinimigo(double x, double y){
    if ((0<=y && y<=279) && (380<=x && x<=420))
        return 1;
    if ((319<=y && y<=600) && (380<=x && x<=420))
        return 2;
    if ((0<=x && x<=379) && (280<=y && y<=320))
        return 3;
    else
        return 4;
}
int resumocodigo(double um, double dois, double umneg, double doisneg){
    if ((380<=umneg && umneg<=420 && 280<=dois && dois<=320) || (380<=um && um<=420 && 280<=doisneg && doisneg<=320) || (380<=umneg && umneg<=420 && 280<=doisneg && doisneg<=320) || (380<=um && um<=420 && 280<=dois && dois<=320))
        return 1;
}