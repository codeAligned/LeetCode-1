### Blackrock

#### My Online Assesment

*   Portfolio and Benchmark
    *   Use Java OO design

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Portfolio {
    private String ticker;
    private String name;
    private String quantity;
    private String price;
    private String value;
    private String nav;
    
    Portfolio (String t, String n, Double q, Double p, Double v) {
        ticker = t;
        name = n;
        quantity = String.format("%.0f", q);
        price = String.format("%.2f", p);
        value = String.format("%.2f", v);
        nav = String.format("%.2f", nav);
    }
    
    Portfolio (String t, String n, String q) {
        ticker = t;
        name = n;
        quantity = q;
    }
    
    Portfolio (String t, String n, String q, String p) {
        ticker = t;
        name = n;
        quantity = q;
        price = p;
    }
    
    public String getTicker() {
        return ticker;
    }
    
    public void setTicker(String t) {
        this.ticker = t;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String n) {
        this.name = n;
    }
    
    public String getQuantity() {
        return quantity;
    }
    
    public void setQuantity(String q) {
        this.quantity = q;
    }
    
    public String getPrice() {
        return price;
    }
    
    public void setPrice(String p) {
        this.price = p;
    }
    
    public String getValue() {
        return value;
    }
    
    public void setValue(String v) {
        this.value = v;
    }
    
    public String getNav() {
        return nav;
    }
    
    public void setNav(Double nav) {
        this.nav = String.format("%.2f", nav);
    }
    
    public String getStr() {
        return ticker + ", " + name + ", " + quantity + ", " + price + ", " + 
        value + ", " + nav;
    }
}

class PC implements Comparator<Portfolio> {
    @Override
    public int compare(Portfolio p1, Portfolio p2) {
        return p1.getTicker().compareTo(p2.getTicker());
    }
}

class Transaction {
    private String type;
    private String ticker;
    private String quantity;
    
    Transaction (String t, String tk, Double q) {
        type = t;
        ticker = tk;
        quantity = String.format("%.2f", q);
    }
        
    public String getType() {
        return type;
    }
    
    public void setType(String t) {
        this.type = t;
    }
    
    public String getTicker() {
        return ticker;
    }
    
    public void setTicker(String t) {
        this.ticker = t;
    }

    public String getQuantity() {
        return quantity;
    }
    
    public void setQuantity(String q) {
        this.quantity = q;
    }
    
    public String getStr() {
        return type + ", " + ticker + ", " + quantity;
    }
}

class TC implements Comparator<Transaction> {
    @Override
    public int compare(Transaction t1, Transaction t2) {
        return t1.getTicker().compareTo(t2.getTicker());
    }
}

public class Main {
    
	public static final String SEPARATOR = "@";
    public static final String COLON = ":";
    
    /*
     * Complete the function below.
     *
 	 * Note: The questions in this test build upon each other. We recommend you
	 * copy your solutions to your text editor of choice before proceeding to
	 * the next question as you will not be able to revisit previous questions.
	 */


    static String generateTransactions(String inputString) {
        inputString.trim();
        String [] pfl_bm = inputString.split(COLON);
        StringTokenizer st = new StringTokenizer(pfl_bm[0], SEPARATOR);
        StringTokenizer st2 = new StringTokenizer(pfl_bm[1], SEPARATOR);
        ArrayList<Portfolio> pal = new ArrayList();
        while (st.hasMoreTokens()) {
            String [] strs = st.nextToken().split(",");
            Portfolio pfl = new Portfolio(strs[0], strs[1], strs[2]);
            pal.add(pfl);
        }
        Collections.sort(pal, new PC());
        ArrayList<Portfolio> bmal = new ArrayList();
        while (st2.hasMoreTokens()) {
            String [] strs = st2.nextToken().split(",");
            Portfolio pfl = new Portfolio(strs[0], strs[1], strs[2], strs[3]);
            bmal.add(pfl);
        }
        Collections.sort(bmal, new PC());
        Double bm_val = 0.0;
        Double pfl_val = 0.0;
        for (int i = 0; i < pal.size(); i++) {
            Portfolio p1 = pal.get(i);
            Portfolio p2 = bmal.get(i);
            Double p = Double.parseDouble(p2.getPrice());
            Double pfl_q = Double.parseDouble(p1.getQuantity());
            Double bm_q = Double.parseDouble(p2.getQuantity());
            pfl_val += pfl_q * p;
            bm_val += bm_q * p;
        }
        ArrayList<Transaction> tal = new ArrayList();
        for (int i = 0; i < pal.size(); i++) {
            Portfolio p1 = pal.get(i);
            Portfolio p2 = bmal.get(i);
            String t = p1.getTicker();
            Double p = Double.parseDouble(p2.getPrice());
            Double q1 = Double.parseDouble(p1.getQuantity());
            Double q2 = Double.parseDouble(p2.getQuantity());
            Double rel = q2 * p / bm_val;
            Transaction trans;
            Double q = rel * pfl_val / p - q1;
            if (q > 0) {
                trans = new Transaction("BUY", t, q);
            } else {
                trans = new Transaction("SELL", t, q);
            }
            tal.add(trans);
        }
        Collections.sort(tal, new TC());
        String str = "";
        for (Transaction t: tal) {
            str += ", [" + t.getStr() + "]";
        }
        return str.substring(2);
    }
    
    public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        String res;
        String _input;
        try {
            _input = in.nextLine();
        } catch (Exception e) {
            _input = null;
        }
        res = generateTransactions(_input);
        System.out.println(res);
    }
}
```