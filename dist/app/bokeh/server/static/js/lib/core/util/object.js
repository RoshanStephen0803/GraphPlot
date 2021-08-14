import { concat, union } from "./array";
export const { keys, values, entries, assign: extend } = Object;
export function clone(obj) {
    return Object.assign({}, obj);
}
export function merge(obj1, obj2) {
    /*
     * Returns an object with the array values for obj1 and obj2 unioned by key.
     */
    const result = Object.create(Object.prototype);
    const keys = concat([Object.keys(obj1), Object.keys(obj2)]);
    for (const key of keys) {
        const arr1 = obj1.hasOwnProperty(key) ? obj1[key] : [];
        const arr2 = obj2.hasOwnProperty(key) ? obj2[key] : [];
        result[key] = union(arr1, arr2);
    }
    return result;
}
export function size(obj) {
    return Object.keys(obj).length;
}
export function isEmpty(obj) {
    return size(obj) == 0;
}
export function to_object(map) {
    const obj = {};
    for (const [key, val] of map) {
        obj[key] = val;
    }
    return obj;
}
//# sourceMappingURL=object.js.map