
price = [('Laptop', '50000.67'), ('Book', '341.78'), ('Pen ','12.23'),('Keyboard ','412.3'),('Mouse','300.43'),('Computer Cable','456.4'),('Mobile','10056.4'),('Software ','950.4'),('Window  ',' 10000.4'),('Computer chips','35000.4')]
print('\n',sorted(price, key=lambda x: float(x[1])))
