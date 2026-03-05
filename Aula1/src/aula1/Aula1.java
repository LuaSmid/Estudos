
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula1;
//im0port java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author alunocmc
 */
public class Aula1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
    //Locale.setDefault(Locale.US);
    
    Scanner scan = new Scanner(System.in);
    
    System.out.println("Digite um nome: ");
        
    String nome = scan.nextLine();
    
    System.out.println("Digite sua idade: ");
    /* sout + tab*/
    int idade = scan.nextInt();
    
    if(idade >= 18) {
        
    System.out.println("Digite seu salario/hora: ");
    double salarioHora = scan.nextDouble();
    
    //Salario semanal (44 horas)
    double resultado = (salarioHora * 44);
    
    //Descontar 15% de IRRF
    double IRRFresultado = resultado * (1 - 0.15);
    System.out.printf("Salario Semanal descontado do IRRF %.2f %n", IRRFresultado);
    
    //Descontar 10% de INSS
    double INSSresultado = resultado * (1 - 0.10);
    System.out.printf("Salario Semanal descontado do INSS %.2f %n", INSSresultado);
    
    //Salário Bruto sem descontos
    double brutoresultado = resultado - IRRFresultado - INSSresultado;
    System.out.printf("Salario Semanal Liquido %.2f %n", brutoresultado);
    }else
      System.out.println("Criança");
        
    System.out.println("Meu nome e " + nome + " e eu tenho " + idade + " anos");
    
    }
    
}