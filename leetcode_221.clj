(defn solution [first-digits second-digits]
  (loop [first-digits first-digits
         second-digits second-digits
         carray-digit 0
         result '()]
    (let [first-digit (or (first first-digits) 0)
          second-digit (or (first second-digits) 0)
          sum (+ carray-digit
                 (+ first-digit second-digit))]
      (if (and
           (nil? (first first-digits))
           (nil? (first second-digits)))
        result
        (recur (rest first-digits)
               (rest second-digits)
               (int (/ sum 10))
               (concat result
                       [(mod sum 10)]))))))

(assert
 (= (solution '(1 9) '(3 4 5))
    '(4 3 6)))

(assert
 (= (solution '(1 2) '(3 4 5))
    '(4 6 5)))

(assert
 (= (solution '(1 2 3) '(3 4 5))
    '(4 6 8)))

(println "Pass!")
