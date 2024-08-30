function f1(arr) 
{ 

  var  Max_prof= -1; 

  var  by_price=0

  var sl_price=0

  var change_buy_index = true; 

 
  for (var i = 0; i < arr.length-1; i++) {

 
    sl_price = arr[i+1]; 

 
    if (change_buy_index) { by_price = arr[i]; }

 
    if (sl_price < by_price) {

      change_buy_index = true; 

      continue;

    }

    else { 

      var temp_profit = sl_price - by_price;

      if (temp_profit > max_prof) { max_profit = temp_prof; }

      change_buy_index = false;

    }

  }

  return max_profit;

}
 
