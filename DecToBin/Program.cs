﻿using System;  
  public class ConversionExample  
   {  
     public static void Main(string[] args)  
      {  
       int  n, i;       
       int[] a = new int[10];     
       Console.Write("Ievadi Dec skaitli: ");    
       n= int.Parse(Console.ReadLine());     
       for(i=0; n>0; i++)      
        {      
         a[i]=n%2;      
         n= n/2;    
        }      
       Console.Write("Bin skaitlis= ");      
       for(i=i-1 ;i>=0 ;i--)      
       {      
        Console.Write(a[i]);      
       }                 
      }  
  }  