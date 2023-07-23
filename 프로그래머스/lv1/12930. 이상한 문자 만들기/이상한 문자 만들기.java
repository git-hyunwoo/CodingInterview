import java.util.ArrayList;

class Solution {
    public String solution(String s) {
        String answer = "";
        ArrayList<String> strArrayList = new ArrayList<>();
        
        String[] strArr = s.split(" ");
        
        for(String tmp : strArr){
            System.out.print(">>>" + tmp);
        }
        
        
        for(String word : strArr){
            String tmp_word = "";
            for(int i = 0; i < word.length(); i++){
                if(i % 2 == 0){
                    tmp_word += (word.charAt(i) + "").toUpperCase();
                }else if(i % 2 != 0){
                    tmp_word += (word.charAt(i) + "").toLowerCase();
                }else if((word.charAt(i) + "").equals(" ")){
                    System.out.println("hello world~!");
                }
                
            }
            strArrayList.add(tmp_word);
            
        }
        
        
        answer = String.join(" ", strArrayList);
        
        return answer;
    }
}