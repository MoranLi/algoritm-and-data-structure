class solution{
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