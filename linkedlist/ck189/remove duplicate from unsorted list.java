class solution{
  /**
   * solution from leetcode 26
   * two pointer algoritm
   * @param list list that need to remove duplicate element
   * @return new length of list
   * loop through list
   * each time find a element different from original element
   * means the elements between i and k is same
   * so set next element to value of k 
   * and move i to the next
   */
  public int twoPointersolution(LinkedList<Integer> list){
    Collections.sort(list);
    int i =  0;
    for(int k=0;k<list.size();k++){
      if(list.get(k) != list.get(i)){
        i++;
        list.set(i,list.get(k));
      }
    }
    return i+1;
  }
}