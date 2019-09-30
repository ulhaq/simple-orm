public class Order {
    private String date;
    private int total;
    private int customer_id;
    private List<OrderLine> lines;
                
    public void setDate(String date) {
        this.date = date; 
    }

    public String getDate() {
        return date; 
    }
                
    public void setTotal(int total) {
        this.total = total; 
    }

    public int getTotal() {
        return total; 
    }
                
    public void setCustomer_id(int customer_id) {
        this.customer_id = customer_id; 
    }

    public int getCustomer_id() {
        return customer_id; 
    }
                
    public void setLines(List<OrderLine> lines) {
        this.lines = lines; 
    }

    public List<OrderLine> getLines() {
        return lines; 
    }
}