#include <stdio.h>
// ������������ ������� �� ���������������� ����������� 
// �����, ������������� � ������� ��������
int main(int argc, char * argv[])
{
    FILE * f = fopen("input.txt", "w");
    long i, N;
    if (argc<=1)
       { 
         printf("Max = ");
         scanf("\%ld", &N);
       } 
       else N = atoi(argv[1]);
    for (i = N; i > 0; i--)
       fprintf(f, "\%d ", i);
    fclose(f);
    return 0;
}
