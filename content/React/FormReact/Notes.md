# Notes

## Build user interface with React

1. Break it apart into pieces called components.
2. Describe the different visual states for each of your components.
3. Connect your components together so that the data flows through them.

## Start with a mockup

1. You have json data from api, for example

```json
[
  { "category": "Fruits", "price": "$1", "stocked": true, "name": "Apple" },
  {
    "category": "Fruits",
    "price": "$1",
    "stocked": true,
    "name": "Dragonfruit"
  },
  {
    "category": "Fruits",
    "price": "$2",
    "stocked": false,
    "name": "Passionfruit"
  },
  {
    "category": "Vegetables",
    "price": "$2",
    "stocked": true,
    "name": "Spinach"
  },
  {
    "category": "Vegetables",
    "price": "$4",
    "stocked": false,
    "name": "Pumpkin"
  },
  { "category": "Vegetables", "price": "$1", "stocked": true, "name": "Peas" }
]
```

2. Then you have drawing of your UI to build.

3. Folow 5 steps.

## Five steps

1. Break the UI into a component hierarchy

For example:

- FilterableProductTable
  - SearchBar
  - ProductTable
    - ProductCategoryRow
    - ProductRow

2. Build a static version in React

To build a static version of your app that renders your data model,  
you’ll want to build components that reuse other components and pass data using props.  
Props are a way of passing data from parent to child.  
It’s usually easier to go top-down, and on larger projects, it’s easier to go bottom-up.

```javascript
function ProductCategoryRow({ category }) {
  return (
    <tr>
      <th colSpan="2">{category}</th>
    </tr>
  )
}

function ProductRow({ product }) {
  const name = product.stocked ? (
    product.name
  ) : (
    <span style={{ color: 'red' }}>{product.name}</span>
  )

  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  )
}

function ProductTable({ products }) {
  const rows = []
  let lastCategory = null

  products.forEach((product) => {
    if (product.category !== lastCategory) {
      rows.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category}
        />
      )
    }
    rows.push(<ProductRow product={product} key={product.name} />)
    lastCategory = product.category
  })

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  )
}

function SearchBar() {
  return (
    <form>
      <input type="text" placeholder="Search..." />
      <label>
        <input type="checkbox" /> Only show products in stock
      </label>
    </form>
  )
}

function FilterableProductTable({ products }) {
  return (
    <div>
      <SearchBar />
      <ProductTable products={products} />
    </div>
  )
}

const PRODUCTS = [
  { category: 'Fruits', price: '$1', stocked: true, name: 'Apple' },
  { category: 'Fruits', price: '$1', stocked: true, name: 'Dragonfruit' },
  { category: 'Fruits', price: '$2', stocked: false, name: 'Passionfruit' },
  { category: 'Vegetables', price: '$2', stocked: true, name: 'Spinach' },
  { category: 'Vegetables', price: '$4', stocked: false, name: 'Pumpkin' },
  { category: 'Vegetables', price: '$1', stocked: true, name: 'Peas' },
]

export default function App() {
  return <FilterableProductTable products={PRODUCTS} />
}
```

3. Find the minimal but complete representation of UI state.

Think of state as the minimal set of changing data that your app needs to remember.

- Does it remain unchanged over time? If so, it isn’t state.
- Is it passed in from a parent via props? If so, it isn’t state.
- Can you compute it based on existing state or props in your component?  
  If so, it definitely isn’t state!

Pieces of data in this example application:

1. The original list of products
2. The search text the user has entered
3. The value of the checkbox
4. The filtered list of products

---

1. The original list of products is passed in as props, so it’s not state.
2. The search text seems to be state since it changes over time and can’t be computed from anything.
3. The value of the checkbox seems to be state since it changes over time and can’t be computed from anything.
4. The filtered list of products isn’t state because it can be computed by taking the original list of products  
   and filtering it according to the search text and value of the checkbox.
   This means only the search text and the value of the checkbox are state!

4: Identify where your state should live

React uses one-way data flow, passing data down the component hierarchy from parent to child component.

For each piece of state in your application:

1. Identify every component that renders something based on that state.
2. Find their closest common parent component—a component above them all in the hierarchy.
3. Decide where the state should live:
   1. Often, you can put the state directly into their common parent.
   2. You can also put the state into some component above their common parent.
   3. If you can’t find a component where it makes sense to own the state,  
      create a new component solely for holding the state  
      and add it somewhere in the hierarchy above the common parent component.

Example:

1. ProductTable needs to filter the product list based on that state (search text and checkbox value).
   SearchBar needs to display that state (search text and checkbox value).
2. The first parent component both components share is FilterableProductTable.
3. We’ll keep the filter text and checked state values in FilterableProductTable.

Add state to the component with the useState() Hook.  
Hooks are special functions that let you “hook into” React.

Add two state variables at the top of FilterableProductTable and specify their initial state:

```javascript
function FilterableProductTable({ products }) {
  const [filterText, setFilterText] = useState('');
  const [inStockOnly, setInStockOnly] = useState(false);
```

Then, pass filterText and inStockOnly to ProductTable and SearchBar as props:

```javascript
<div>
  <SearchBar filterText={filterText} inStockOnly={inStockOnly} />
  <ProductTable
    products={products}
    filterText={filterText}
    inStockOnly={inStockOnly}
  />
</div>
```

5. Add inverse data flow.

Currently your app renders correctly with props and state flowing down the hierarchy.  
But to change the state according to user input, you will need to support data flowing the other way:  
the form components deep in the hierarchy need to update the state in FilterableProductTable.

If you try to type or check the box in the example above,  
you’ll see that React ignores your input. This is intentional.  
By writing <input value={filterText} />, you’ve set the value prop  
of the input to always be equal to the filterText state passed in from FilterableProductTable.  
Since filterText state is never set, the input never changes.

You want to make it so whenever the user changes the form inputs,  
the state updates to reflect those changes. The state is owned by FilterableProductTable,  
so only it can call setFilterText and setInStockOnly.  
To let SearchBar update the FilterableProductTable’s state,  
you need to pass these functions down to SearchBar:

```javascript
function FilterableProductTable({ products }) {
  const [filterText, setFilterText] = useState('');
  const [inStockOnly, setInStockOnly] = useState(false);

  return (
    <div>
      <SearchBar
        filterText={filterText}
        inStockOnly={inStockOnly}
        onFilterTextChange={setFilterText}
        onInStockOnlyChange={setInStockOnly} />
```

Inside the SearchBar, you will add the onChange  
event handlers and set the parent state from them:

```javascript
function SearchBar({
  filterText,
  inStockOnly,
  onFilterTextChange,
  onInStockOnlyChange
}) {
  return (
    <form>
      <input
        type="text"
        value={filterText}
        placeholder="Search..."
        onChange={(e) => onFilterTextChange(e.target.value)}
      />
      <label>
        <input
          type="checkbox"
          checked={inStockOnly}
          onChange={(e) => onInStockOnlyChange(e.target.checked)}
```
