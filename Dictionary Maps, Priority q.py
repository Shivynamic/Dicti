#!/usr/bin/env python
# coding: utf-8

# In[2]:


class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
class Map:
    def __init__(self):
        self.bucketSize =10
        self.Bucket = [None for i in range(self.bucketSize)]
        self.count=0
        
    def size(self):
        return self.count
    
    def getindexvalue(self,hc):
        return (abs(hc) % self.bucketSize)
    
    
    def getValue(self,key):
        hc = hash(key)
        index = getindexvalue(hc)
        head= self.Bucket[index]
        while head is not None:
            if head.key==key:
                return head.value
            head = head.next
        return None
    def remove(self,key):
        hc = hash(key)
        index=getindexvalue(hc)
        head = self.Bucket[index]
        prev = None
        while head is not None:
            if head.key==key:
                if prev is None:
                    self.Bucket[index] = head.next
                else:
                    prev.next = head.next
                self.count-=1
                return head.value
                prev = head
                head = head.next
        return None
        
        
    
    def insert(self,key,value):
        hc = hash(key)
        index= getindexvalue(hc)
        head = self.Bucket[index]
        while head is not None:
            if head.key==key:
                head.value = value
                return 
            head = head.next
        head = self.Bucket[index]
        newNode = Mapnode(key,value)
        newNode.next = head
        self.Bucket[index]=newNode
        self.count+=1

        


# In[ ]:





# In[ ]:


class priorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class priorityQueue:
    def __init__(self):
        self.pq = []
    
    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize==0
    
    def getMin(self):
        if self.isEmpty()==True:
            return None
        return self.pq[0].value
    def __percolateUp(self):
        childindex = self.getSize()-1
        while childindex>0:
            parentIndex = (childindex-1)//2
            if self.pq[childindex].priority < self.pq[parentIndex].priority:
                self.pq[childindex],self.pq[parentIndex]=self.pq[parentIndex], self.pq[childindex]
                childindex = parentIndex
            else:
                break                
        
    def insert(self,value):
        pqNode = priorityQueueNode(value)
        self.pq.append(pqNode)
        self.__percolateUp()
        
        
        
    def __percolateDown(self):
        parentIndex = 0
        leftchildIndex = 2*parentIndex+1
        rightchildIndex = 2*parentIndex+2
        while leftchildIndex < self.getSize(): 
            minIndex = parentIndex
            if self.pq[minIndex].priority<self.pq[leftchildIndex].priority:
                minIndex = leftchildIndex  
            if rightchildIndex<self.getSize() and self.pq[minIndex].priority<self.pq[rightchildIndex].priority:
                minIndex = rightchildIndex
            if minIndex==parentIndex:
                break
            self.pq[parentIndex],self.pq[minIndex]=self.pq[minIndex],self.pq[parentIndex]
            parentIndex = minIndex
            leftchildIndex = 2*parentIndex+1
            rightchildIndex = 2*parentIndex+2
            
    
                
        
    
        
    def remove(self,value):
        if self.isEmpty== True:
            return None
        
        ele = self.pq[0]
        self.pq[0]= self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele
        
        
        


# # Heap Sort
# 
# 

# In[ ]:


def heapify(arr,i,n):
    parentIndex =i
    leftchildIndex = 2*parentIndex +1
    rightchildIndex = 2*parentIndex +2
    while leftchildIndex<n:
        minIndex = parentIndex
        if arr[minIndex]>arr[leftchildIndex]:
            minIndex = leftchildIndex
        if rightchildIndex<n and arr[minIndex]>arr[rightchildIndex]:
            minIndex = rightchildIndex
        
        arr[minIndex],arr[parentIndex] = arr[parentIndex],arr[minIndex]
        parentIndex = minIndex  
        leftchildIndex = 2*parentIndex+1
        rightchildIndex = 2*parentIndex+2
    
    return
        
    
    
def HeapSort(arr):
    n = len(arr)
    for i in range((n//2)-1,-1,-1):
        heapify(arr,i,n)
        
    for j in range(n-1,0,-1):
        arr[0],arr[j]=arr[j],arr[0]
        heapify(arr,0 ,j)
    return
        
    


# In[9]:


# k smallest element
import heapq
def kSmallest(arr,k):
    heap = arr[:k]
    heapq._heapify_max(heap)
    n = len(arr)
    for i in range(k,n):
        if heap[0]>arr[i]:
            heapq._heapreplace_max(heap,arr[i])
    return heap

arr = [55, 44, 46, 89, 10, 21, 1,2,5,4,6,88]
re = kSmallest(arr,4)
for i in re:
    print(i,end=" ")
print()
print(re)


# # Huffman coding
# 

# In[ ]:


# characters with more frequemcy will have to occupy less space and vice versa for characters with minimum freq


# pick min freq pair
# using hash map


# In[3]:


import heapq
class binaryTreeNode:
    def __init__(self,val,freq):
        self.value = val
        self.freq = freq
        self.left = None
        self.right = None

class Huffmancoding:
    def __init__(self,path):
        self.path = path
    
    def __make_frequency_dict(self,text):
        d ={}
        for i in text:
            if i not in d:
                d[i]=0
            d[i]+=1
        return d
    def __buildHeap(self,freqdict):
        for key in freqdict:
            freqq = freqdict[key]
            binarytreenode = binaryTreeNode(key,freqq)
            heapq.heappush(self.__push, binarytreenode)
            
        
        
    def __buildTree(self):
        while len(self.__heap)>1:
            binarytreenode1 = heapq.heappop(self.__heap)
            binarytreenode2 = heapq.heappop(self.__heap)
            freqsum = freqnode1.freq + freqnode2.freq
            newNode = binaryTreeNode(None,freqsum)
            newNode.left = binarytreenode1
            newNode.right = binarytreenode2
            heapq.heappush(self.__heap,newNode)
        return
    
    def __getEncodedText(self,text):
        encoded_text = ""
        for char in text:
            encoded_text+=self.__codes[char]
        return encoded_text
    def __buildCodesHelper(self,root,curr_bits):
        if root == None:
            return
        if root.value is not None:
            self.__codes[root.value]=curr_bits
            return        
        self.__buildCodesHelper(root.left,curr_bits+"0")
        self.__buildCodesHelper(root.right,curr_bits+"1")
        
    
    def __buildCodes(self):
        root = heapq.heappop(self.__heap)
        return self.__buildCodesHelper(root,"")
    
    def __getPaddedEncodedText(self,encoded_text):
        paddedamount = 8 - (len(encoded_text)%8)
        for i in range(paddedamount):
            encoded_text+='0'
        padded_info = "{0.08b}".format(paddedamount)
        padded_encoded_text = padded_info+encoded_text
        return padded_encoded_text
    
    def __getBytesArray(self,padded_encoded_text):
        array=[]
        for i in range(0,len(padded_encoded_text),8):
            byte = padded_encoded_text[i:i+8]
            array.append(int(byte,2))
        return array
    
        
    def compress(self,text):
#         get file from path
#         red text from file
        text = 'ajdshjfajdfheihfegnjkegn'
#     make frequency dictionary using the text
        freq_dict = self.__make_frequency_dict(text)
#     Construct the heap from the frequency dictionary
        
        self.__buildHeap(freq_dict)
#         Construct binary tree from the heap
        
        self.__buildTree()
#         construct the codes from binary tree
        self.__buildCodes()
#     creating the encoded text using the codes
        encoded_text = self.__buildCodesHelper()
    
#  put this encoded text into a binary tree
#         pad encoded text
        padded_encoded_text = self.__getPaddedEncodedText(encoded_text)
#     converting it into array that stores bytes value
        bytes_array = self.__getBytesArray(padded_encoded_text)
        final_bytes = bytes(bytes_array)
    

#         return this binary file as output
        pass
    


# In[5]:


print(int("0101",2))


# In[ ]:




