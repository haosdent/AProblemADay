(defn solution [coll n]
  (loop [result '()
         p coll]
    (if (nil? (first p))
      result
      (recur (concat result
                     (if (< (count p) n)
                       p
                       (reverse (take n p))))
             (nthrest p n)))))

(assert
 (= (solution '(1 2 3 4 5) 2)
    '(2 1 4 3 5)))

(assert
 (= (solution '(1 2 3 4 5) 3)
    '(3 2 1 4 5)))

(assert
 (= (solution '(1 2 3 4 5 6) 2)
    '(2 1 4 3 6 5)))

(println "Pass!")
