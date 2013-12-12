(defn solution [coll]
  (let [uniq (fn [pre item]
               (if (= (last pre) item)
                 pre
                 (concat pre [item])))]
    (reduce uniq '()  coll)))

(assert
 (= (solution '(1 2 2 3 4 5))
    '(1 2 3 4 5)))

(assert
 (= (solution '(1 2 3 4 5))
    '(1 2 3 4 5)))

(println "Pass!")
