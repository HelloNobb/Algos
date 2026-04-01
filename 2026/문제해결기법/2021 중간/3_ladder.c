#include <stdio.h>
#include <stdlib.h>

int m, n;

int down_ladder(int row, int start, int **G){
	// end-point
	if (row == n){
		return start;
	}
	int nextL = start-1;
	int nextR = start;
	int nextRow = row+1;

	if (nextL >= 0 && G[row][nextL] == 1){
		return down_ladder(nextRow, start-1, G);

	} 
	else if (nextR < m-1 && G[row][nextR] == 1){
		return down_ladder(nextRow, start+1, G);
	} 
	else {
		return down_ladder(nextRow, start, G);
	}
}

int main(void)
{
	// input ====
	int from; //열 개수, 행 개수, 시작 행번호
	scanf("%d %d", &m, &n);
	scanf("%d", &from);
	
	// 동적 할당으로 n*m 2차배열 공간 할당받기
	int **GRAPH = (int**)malloc(sizeof(int*)*n);
	
	for (int i = 0; i < n; i++){
		GRAPH[i] = (int*)malloc(sizeof(int)*m);
	}
	
	// 각 자리에 입력받은 것 중 1개의 정수씩 끊어 배열에 담기
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m-1; j++){
			scanf("%1d", &GRAPH[i][j]);
		}
	}
	
	// output ====
	int rslt = down_ladder(0, from, GRAPH);
	printf("%d", rslt);

	// 2차배열 free 처리 ====
	for (int i = 0; i < n; i++){
		free(GRAPH[i]);
	}
	free(GRAPH);

	return 0;
}