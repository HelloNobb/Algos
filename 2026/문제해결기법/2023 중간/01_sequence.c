#include <stdio.h>
#include <stdlib.h>

int is_sequence(int n, int* arr){
	int memory = -1;
	for (int i = 0; i < n-1; i++){

		int GAP = arr[i+1] - arr[i];

		if (memory == -1){
			memory = GAP;
		}
		if (GAP != memory){
			return 0;
		}
	}
	return 1;
}

int main(void){

	int N;
	scanf("%d", &N);
	
	int* ARR = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++){
		scanf("%d", &ARR[i]); //C scanf: 공백 알아서 건너뛰고 버퍼 숫자만 찾아옴
	}

	printf("%d", is_sequence(N, ARR));
	
	free(ARR);
}