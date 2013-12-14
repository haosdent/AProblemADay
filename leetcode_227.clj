(defn solution [coll]
  (loop [result '()
         p coll]
    (let [x (rest p)
          y (rest x)]
      (if (nil? (first p))
        result
        (recur (concat result
                       (if (nil? (first x))
                         nil
                         [(first x)])
                       [(first p)])
               y)))))

(assert
 (= (solution '(1 2 3 4 5))
    '(2 1 4 3 5)))

(assert
 (= (solution '(1 2 3 4 5 6))
    '(2 1 4 3 6 5)))

(println "Pass!")
