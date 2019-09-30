public class OrderLine {
    private int order_id;
    private int product_id;
    private int count;
    private int total;
                
    public void setOrder_id(int order_id) {
        this.order_id = order_id; 
    }

    public int getOrder_id() {
        return order_id; 
    }
                
    public void setProduct_id(int product_id) {
        this.product_id = product_id; 
    }

    public int getProduct_id() {
        return product_id; 
    }
                
    public void setCount(int count) {
        this.count = count; 
    }

    public int getCount() {
        return count; 
    }
                
    public void setTotal(int total) {
        this.total = total; 
    }

    public int getTotal() {
        return total; 
    }
}