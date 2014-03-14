#include "global.h"
#include<stdlib.h>
#include<stdio.h>
int comp (const void * elem1, const void * elem2) 
{
    int f = *((int*)elem1);
    int s = *((int*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}

float* copy(float* t,int size)
{
 int i,j;
 float *tarray=(float *)malloc(sizeof(float)*size);
 for(i=0;i<size;i++)
   tarray[i]=t[i];
 return tarray;
}
int** TCPdetermineOptimalBands(float* A, int N, int K)
{
int i,j,k,a,b;
float J[N];
float Js[K-1];
float upper = 0, lower = 0, nelements = 0;
float I[K-1];
float Is[K-1];
float* temp;
int band[N][N];
float As[N];

As = copy(A,N);
 qsort(As,sizeof(As)/sizeof(*As), sizeof(*As), comp);

for(i=0;i<N;i++)
  J[i] = As[i] - As[i+1];

temp = copy(J,N-1);
qsort(temp,sizeof(temp)/sizeof(*temp), sizeof(*temp), comp);

for(i=0;i<K-1;i++)
  Js[i]=temp[i];

for(i=0,j=0;i<N;i++)
  if(Js[i] == J[i])
  {
  I[j]=i;
  j++;
  }
  
Is = copy(I,K-1);
qsort(Is,sizeof(Is)/sizeof(*Is), sizeof(*Is), comp);

for(i=0;i<K-1;i++)
  {
  upper =Is[i];
  nelements = upper - lower + 1;
  k=0;
  band[i][k++] = nelements;
  for(j=lower;j<lower+nelements;j++)
    for(a=0,b=0;a<N;a++)
      if(As[j] == A[a])
      {
      band[i][k++] = a;
      temp[b]=a;
      b++;
      }
  lower = upper + 1;
  }
for(a=0;a<N;a++)
 {
 if(temp[a]==a)
  continue;
 band[i][k++]=a;
 }
 return band; 
}


int main()
{ float a[]={500,291,271,36,222,111,1211,3,1,31,1};
  int band[10][10]={-1};
  int i,j;
  band=TCPdetermineOptimalBands(a, 10, 5);
  for(i=0;i<10;i++)
   {
   for(j=0;j<10;j++)
   	{if(band[i][j]==-1)continue;
   	printf("%d\t",band[i][j]);
    }
    printf("\n");
   }
   return 0; 
}