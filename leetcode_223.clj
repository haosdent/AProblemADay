(defn solution [coll x]
  (concat
   (filter #(< % x) coll)
   (filter #(>= % x) coll)))

(assert
 (= (solution '(1 4 3 2 5 2) 3)
    '(1 2 2 4 3 5)))

(println "Pass!")
