import java.util.Scanner;

public class IncreaseAndCopy {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int t = Integer.parseInt(sc.nextLine());
    for(int z = 0; z < t; z++){
      int n = Integer.parseInt(sc.nextLine());
      int exponente = 1;
      int resultado = 0;
      while(n > exponente * exponente){
        resultado += 2;
        exponente++;
      }
      double raiz = Math.sqrt(n);
      if(n != 1 && raiz % Math.floor(raiz) < 0.5 && n != exponente*exponente)
        resultado--;
      System.out.println(resultado);
    }
  }
}