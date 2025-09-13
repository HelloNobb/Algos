#알파벳 소문자-사전식 정렬방법: 아스키?
import sys
input = sys.stdin.readline

N = int(input()) #단어 개수

## 중복제거작업 ============
words = set() #중복 제거 위해 일단 set형으로 (-후에 list로 변환)
for i in range(N):
	words.add(input().strip())	#중복 자동제거 + stip:공백모두제거(원하는거)

words = list(words)

words.sort(key=lambda w : (len(w), w)) #길이-값(단어) 쌍 튜플로 정렬 (앞(길이) -> 뒤(단어데이터) 순으로 비교정렬함)
for w in words:
    sys.stdout.write(w+"\n")
#### 참고 ======
# 중복제거  -  set(=중복없는집합)