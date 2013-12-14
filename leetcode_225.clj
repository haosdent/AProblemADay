(defn solution [coll]
  (loop [result '()
         coll coll]
    (let [item (first coll)
          coll (if (= item
                      (first (rest coll)))
                 (drop-while #(= item %) coll)
                 coll)]
      (if (nil? (first coll))
        result
        (recur (concat result [(first coll)])
               (rest coll))))))

(assert
 (= (solution '(1 2 2 3 4 5))
    '(1 3 4 5)))

(assert
 (= (solution '(1 2 3 4 5))
    '(1 2 3 4 5)))

(assert
 (= (solution '(1 2 3 3 4 5 5))
    '(1 2 4)))

(println "Pass!")
