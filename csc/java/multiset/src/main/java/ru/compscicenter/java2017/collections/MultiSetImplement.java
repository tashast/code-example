package ru.compscicenter.java2017.collections;

import java.util.*;



/**
 * MultiSet is an unordered collection that may contain duplicate elements.
 * It refines some of the operations inherited from {@link Collection}
 * and adds several new operations aware of MultiSet's ability to contain multiple
 * occurrences of an element.
 *
 * Implementations must provide default constructor (without arguments)
 * and constructor with single argument of type <code>Collection&lt;? extends E&gt;</code>.
 *
 * @param <E> the type of elements in this multiset
 */


public class MultiSetImplement<E> extends AbstractCollection<E> implements MultiSet<E> {
    private Map<E, Integer> mapSet;

    public MultiSetImplement() {
        this.mapSet = new HashMap<E, Integer>();
    }

    public MultiSetImplement(Collection<? extends E> es) {
        this.mapSet = new HashMap<E, Integer>();
        for (E obj : es) {
            add(obj);
        }
    }



    /**
     * Returns the number of elements in this multiset, including all duplicates
     *
     * @return the number of elements in this multiset, including all duplicates
     */
    @Override
    public int size() {
        int sizeSet = 0;
        for (E key: mapSet.keySet()) {
            sizeSet += mapSet.get(key);
        }
        return sizeSet;
    }


    /**
     * Returns an iterator over the elements in this multiset.
     * Elements that occur multiple times in the multiset will be returned multiple times
     * by this iterator, but the order is not defined.
     *
     * @return an <tt>Iterator</tt> over the elements in this multiset
     */
    @Override
    public final Iterator<E> iterator() {
       return new MultiSetIterator();
    }


    /**
     * Adds a single occurrence of the specified element to this multiset.
     *
     * Always returns <code>true</code>, because multiset always allows adding
     * both new elements and new occurrences of known elements.
     *
     * @param e  element to add
     * @return <code>true</code>
     */
    @Override
    public boolean add(E e) {
        add(e, 1);
        return true;
    };


    /**
     * Adds multiple occurrences of the specified element to this multiset.
     *
     * @param e           element to add
     * @param occurrences number of element occurrences to add; can't be negative
     * @return the count of element occurrences before the operation; possibly zero
     * @throws IllegalArgumentException if <code>occurrences</code> is negative
     */
    public final int add(E e, int occurrences) {
        if (occurrences < 0) {
            throw new IllegalArgumentException();
        }
        int occurencesBefore;
        if (mapSet.containsKey(e)) {
            occurencesBefore = mapSet.get(e);
            mapSet.put(e, (occurrences + occurencesBefore));
        } else {
            occurencesBefore = 0;
            mapSet.put(e, occurrences);
        }
        return occurencesBefore;
    }


    /**
     * Removes a single occurrence of the specified element from this multiset, if present.
     *
     * @param e element to remove
     * @return <code>true</code> if the element was found and removed
     */
    @Override
    public final boolean remove(Object e) {
        int occurencesBefore;
        if (mapSet.containsKey(e)) {
            occurencesBefore = mapSet.get(e);
            if (occurencesBefore == 1) {
                mapSet.remove(e);
                return true;
            } else {
                mapSet.put((E) e, (occurencesBefore - 1));
                return true;
            }
        } else {
            return false;
        }
    }

    /**
     * Removes multiple occurrences of the specified element from this multiset, if present.
     * If multiset contains fewer copies of the element than given by <code>occurrences</code>
     * parameter, all occurrences are removed.
     *
     * @param e           element to remove
     * @param occurrences number of element occurrences to remove; can't be negative
     * @return the count of element occurrences before the operation; possibly zero
     * @throws IllegalArgumentException if <code>occurrences</code> is negative
     */
    public final int remove(Object e, int occurrences) {
        if (occurrences < 0) {
            throw new IllegalArgumentException();
        }
        int occurencesBefore;
        if (mapSet.containsKey(e)) {
            occurencesBefore = mapSet.get(e);
            if (occurencesBefore <= occurrences) {
                mapSet.remove(e);
                return occurencesBefore;
            } else {
                mapSet.put((E) e, (occurencesBefore - occurrences));
                return occurencesBefore;
            }
        } else {
            return 0;
        }
    }


    /**
     * Returns the number of occurrences of an element in this multiset,
     * or <code>0</code> if multiset does not contain this element.
     *
     * @param e the element to whose occurrences are to be returned
     * @return the number of occurrences of an element in this multiset
     */
    public final int count(Object e) {
        if (mapSet.containsKey(e)) {
            return mapSet.get(e);
        } else {
            return 0;
        }
    }


    /**
     * Returns <code>true</code> if this multiset contains at least one occurrence of each element
     * in the specified collection.
     * <p>
     * This method ignores the occurrence count of an element in the two collections; it may still
     * return <code>true</code> even if other collections contains several occurrences of an element
     * and this multiset contains only one.
     *
     * @param c the collection of elements to be looked up in this multiset
     * @return <code>true</code> if this multiset contains at least one occurrence of each element in <code>c</code>
     */
    @Override
    public final boolean containsAll(Collection<?> c) {
        for (Object entryCollection : c) {
            if (!mapSet.containsKey(entryCollection)) {
                return false;
            }
        }
        return true;
    }


    /**
     * Returns an array containing all of the elements in this multiset including all duplicates.
     *
     * @return an array containing all of the elements in this collection
     */
    @Override
    public Object[] toArray() {
        int arrayIndex = 0;
        Object[] arrayOut = new Object[this.size()];
        Iterator<E> entryIterator = this.iterator();
        while (entryIterator.hasNext()) {
            arrayOut[arrayIndex] = entryIterator.next();
            arrayIndex += 1;
        }
        return arrayOut;
    }


    /**
     * Returns an array containing all of the elements in this multiset including all duplicates.
     * The runtime type of the returned array is that of the specified array.
     * If the collection fits in the specified array, it is returned therein.
     * Otherwise, a new array is allocated with the runtime type of the
     * specified array and the size of this collection.
     * <p>
     * <p>If this collection fits in the specified array with room to spare
     * (i.e., the array has more elements than this collection), the element
     * in the array immediately following the end of the collection is set to
     * <tt>null</tt>.  (This is useful in determining the length of this
     * collection <i>only</i> if the caller knows that this collection does
     * not contain any <tt>null</tt> elements.)
     *
     * @param a the array into which the elements of this collection are to be
     *          stored, if it is big enough; otherwise, a new array of the same
     *          runtime type is allocated for this purpose.
     * @return an array containing all of the elements in this collection
     * @throws ArrayStoreException  if the runtime type of the specified array
     *                              is not a supertype of the runtime type of every element in
     *                              this collection
     * @throws NullPointerException if the specified array is null
     */
    @Override
    public <T> T[] toArray(T[] a) {
        if (a == null) {
            throw new NullPointerException();
        }
        if (a.length < this.size()) {
            return (T[]) this.toArray();
        }
        int arrayIndex = 0;
        Iterator<E> entryIterator = this.iterator();
        Arrays.fill(a, null);
        while (entryIterator.hasNext()) {
            a[arrayIndex] = (T) entryIterator.next();
            arrayIndex += 1;
        }
        return a;
    }


    /**
     * For each element in given collection removes <em>all</em> occurrences
     * of the element from this multiset, if present.
     *
     * @param c collection with elements to remove from this multiset
     * @return <code>true</code> if at least one element was found and removed
     */
    @Override
    public final boolean removeAll(Collection<?> c) {
        boolean changed = false;
        for (Object entryCollection: c) {
            if (mapSet.containsKey(entryCollection)) {
                mapSet.remove(entryCollection);
                changed = true;
            }
        }
        return changed;
    }



    /**
     * For each element in given collection retains <em>all</em> occurrences
     * of the element from this multiset, if present.
     *
     * @param c collection with elements to retain in this multiset
     * @return <code>true</code> if at least one element was removed
     */
    @Override
    public final boolean retainAll(Collection<?> c) {
        boolean changed = false;
        for (E entry: mapSet.keySet()) {
            if (!c.contains(entry)) {
                mapSet.remove(entry);
                changed = true;
            }
        }
        return changed;
    }


    /**
     * Removes all of the elements from this multiset.
     * The collection will be empty after this method returns.
     */
    @Override
    public void clear() {
        super.clear();
    }


    /**
     * Compares the specified object with this multiset for equality.
     * Returns true if the given object is also a multiset
     * and contains equal elements with equal counts.
     *
     * @param o object to compare with
     * @return <code>true</code> if this multiset is equal to given object as defined above
     */
    @Override
    public final boolean equals(Object o) {
        if (o instanceof MultiSetImplement) {
            MultiSet<E> objectSet = (MultiSetImplement<E>) o;
            Iterator<E> objectIterator = objectSet.iterator();
            Iterator<E> entryIterator = this.iterator();

            while (objectIterator.hasNext() && entryIterator.hasNext()) {
                E objectElement = objectIterator.next();
                E entryElement = entryIterator.next();

                if (!objectElement.equals(entryElement) || count(objectElement) != count(entryElement)) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }

    @Override
    public final int hashCode() {
        return super.hashCode();
    }


        private class MultiSetIterator implements Iterator<E> {
            private Iterator<E> innerIterator;
            private E currentKey;
            private int currentOccurence;
            private int innerCount;


            public MultiSetIterator() {
                Set<E> mapKey = new HashSet<>(mapSet.keySet());
                innerIterator = mapKey.iterator();
                innerCount = 0;
            }

            @Override
            public boolean hasNext() {
                return currentKey != null && innerIterator.hasNext();
            }

            @Override
            public E next() {
                if (hasNext()) {
                    if (currentKey != null && currentOccurence > innerCount) {
                        innerCount += 1;
                    } else {
                        currentKey = innerIterator.next();
                        currentOccurence = mapSet.get(currentKey);
                        innerCount = 1;
                    }
                }
                return currentKey;
            }
        }


    }
