(defn solution [coll k]
  (loop [result '()
         p coll
         q (nthrest coll k)]
    (if (nil? (first q))
      (concat result (rest p))
      (recur (concat result
                     [(first p)])
             (rest p)
             (rest q)))))


(assert
 (= (solution '(1 2 3 4 5) 2)
    '(1 2 3 5)))

(println "Pass!")
