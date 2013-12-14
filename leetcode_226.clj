(defn solution [coll k]
  (let [l (count coll)
        k (mod k l)
        j (- l k)]
    (concat (nthrest coll j)
            (take j coll))))

(assert
 (= (solution '(1 2 3 4 5) 2)
    '(4 5 1 2 3)))

(assert
 (= (solution '(1 2 3 4 5) 7)
    '(4 5 1 2 3)))

(println "Pass!")
