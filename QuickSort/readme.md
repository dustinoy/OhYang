# QuickSort 作業

---

## 問題描述
現在有一個隨機數字的list且數字順序沒有從小排到大，我們需運用QuickSort來快速整理並使其從小到大從新排列並回傳新的list。

---

## 程式設計架構
> 1. 先設定一個有隨機排列變數的list1
> 2. 然後再設定3個空的list分為left,mid,right，從list1抓第二個數字為基準值去比較，比基準值小的數字放到left，相等的放在mid,大的放在right
> 3. 分類好之後，left跟right再重複跑QuickSort直到不能再跑為止
> 4. 最後把left+mid+right結合起來並回傳就整理完成了

---

## 流程圖
![](https://github.com/dustinoy/ohyang/blob/master/QuickSort/%E6%B5%81%E7%A8%8B%E5%9C%96.jpg)

---

## 實際測試+說明

  - Python 
  
  ![](https://github.com/dustinoy/ohyang/blob/master/QuickSort/%E5%AF%A6%E9%9A%9B%E6%B8%AC%E8%A9%A6%2B%E8%AA%AA%E6%98%8E.jpg)

---

  - Jupyter 
  ![](https://github.com/dustinoy/ohyang/blob/master/QuickSort/%E7%A8%8B%E5%BC%8F%E7%A2%BCJupyter%E7%89%88.jpg)

- 程式碼
    - [版本一](https://github.com/dustinoy/ohyang/blob/master/QuickSort/QuickSort.ipynb)
 
    - [版本二](https://github.com/dustinoy/ohyang/blob/master/QuickSort/QuickSort.py)
