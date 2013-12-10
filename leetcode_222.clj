(defn solution [coll m n]
  (let [m (dec m)
        start (take m coll)
        end (drop n coll)
        mid (take (- n m)
                  (drop m coll))]
    (concat start
            (reverse mid)
            end)))

(assert
 (= (solution '(1 2 3 4 5) 2 4)
    '(1 4 3 2 5)))

(println "Pass!")
