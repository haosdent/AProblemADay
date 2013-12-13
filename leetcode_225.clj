(defn solution [coll]
  (distinct coll))

(assert
 (= (solution '(1 2 2 3 4 5))
    '(1 2 3 4 5)))

(assert
 (= (solution '(1 2 3 4 5))
    '(1 2 3 4 5)))

(assert
 (= (solution '(1 2 3 3 4 5 5))
    '(1 2 3 4 5)))

(println "Pass!")
