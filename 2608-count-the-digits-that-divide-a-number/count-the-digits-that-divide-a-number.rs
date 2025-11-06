impl Solution {
    pub fn count_digits(num: i32) -> i32 {
        let mut count = 0;
        let num_str = num.to_string();

        for ch in num_str.chars() {
            if let Some(d) = ch.to_digit(10) {
                if d != 0 && num % (d as i32) == 0 {
                    count += 1;
                }
            }
         }
        count
    }
}