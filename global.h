typedef struct
{
char *destination_ip;
char *destination_portnum;
int N;
int K;
float t;
int total_windows_in_learning;
int C[6];
float **W;
float threshold_probability;
} TCPstream;
